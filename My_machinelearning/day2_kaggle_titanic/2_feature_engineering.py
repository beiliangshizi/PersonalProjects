#coding:utf-8
import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import sklearn.preprocessing as preprocessing
from sklearn.ensemble import RandomForestRegressor

### 使用 RandomForestClassifier 填补缺失的年龄属性
def set_missing_ages(df):
    # 把已有的数值型特征取出来丢进Random Forest Regressor中
    age_df = df[['Age','Fare', 'Parch', 'SibSp', 'Pclass']]
    # 乘客分成已知年龄和未知年龄两部分
    known_age = age_df[age_df.Age.notnull()].as_matrix()
    unknown_age = age_df[age_df.Age.isnull()].as_matrix()
    # y即目标年龄
    y = known_age[:, 0]
    # X即特征属性值
    X = known_age[:, 1:]
    # fit到RandomForestRegressor之中
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rfr.fit(X, y)
    # 用得到的模型进行未知年龄结果预测
    predictedAges = rfr.predict(unknown_age[:, 1::])
    # 用得到的预测结果填补原缺失数据
    df.loc[ (df.Age.isnull()), 'Age' ] = predictedAges
    return df, rfr
def set_Cabin_type(df):
    df.loc[ (df.Cabin.notnull()), 'Cabin' ] = "Yes"
    df.loc[ (df.Cabin.isnull()), 'Cabin' ] = "No"
    return df

data_train = pd.read_csv("train.csv")
data_train, rfr = set_missing_ages(data_train)
data_train = set_Cabin_type(data_train)
# print data_train
#
#      PassengerId  Survived  Pclass  \
# 0              1         0       3
# 1              2         1       1
# 2              3         1       3
# 3              4         1       1
# 4              5         0       3
# 5              6         0       3
# 6              7         0       1
# 7              8         0       3
# 8              9         1       3
# 9             10         1       2
# 10            11         1       3
# 11            12         1       1
# 12            13         0       3
# 13            14         0       3
# 14            15         0       3
# 15            16         1       2
# 16            17         0       3
# 17            18         1       2
# 18            19         0       3
# 19            20         1       3
# 20            21         0       2
# 21            22         1       2
# 22            23         1       3
# 23            24         1       1
# 24            25         0       3
# 25            26         1       3
# 26            27         0       3
# 27            28         0       1
# 28            29         1       3
# 29            30         0       3
# ..           ...       ...     ...
# 861          862         0       2
# 862          863         1       1
# 863          864         0       3
# 864          865         0       2
# 865          866         1       2
# 866          867         1       2
# 867          868         0       1
# 868          869         0       3
# 869          870         1       3
# 870          871         0       3
# 871          872         1       1
# 872          873         0       1
# 873          874         0       3
# 874          875         1       2
# 875          876         1       3
# 876          877         0       3
# 877          878         0       3
# 878          879         0       3
# 879          880         1       1
# 880          881         1       2
# 881          882         0       3
# 882          883         0       3
# 883          884         0       2
# 884          885         0       3
# 885          886         0       3
# 886          887         0       2
# 887          888         1       1
# 888          889         0       3
# 889          890         1       1
# 890          891         0       3
#
#                                                   Name     Sex        Age  \
# 0                              Braund, Mr. Owen Harris    male  22.000000
# 1    Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.000000
# 2                               Heikkinen, Miss. Laina  female  26.000000
# 3         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.000000
# 4                             Allen, Mr. William Henry    male  35.000000
# 5                                     Moran, Mr. James    male  23.828953
# 6                              McCarthy, Mr. Timothy J    male  54.000000
# 7                       Palsson, Master. Gosta Leonard    male   2.000000
# 8    Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)  female  27.000000
# 9                  Nasser, Mrs. Nicholas (Adele Achem)  female  14.000000
# 10                     Sandstrom, Miss. Marguerite Rut  female   4.000000
# 11                            Bonnell, Miss. Elizabeth  female  58.000000
# 12                      Saundercock, Mr. William Henry    male  20.000000
# 13                         Andersson, Mr. Anders Johan    male  39.000000
# 14                Vestrom, Miss. Hulda Amanda Adolfina  female  14.000000
# 15                    Hewlett, Mrs. (Mary D Kingcome)   female  55.000000
# 16                                Rice, Master. Eugene    male   2.000000
# 17                        Williams, Mr. Charles Eugene    male  32.066493
# 18   Vander Planke, Mrs. Julius (Emelia Maria Vande...  female  31.000000
# 19                             Masselmani, Mrs. Fatima  female  29.518205
# 20                                Fynney, Mr. Joseph J    male  35.000000
# 21                               Beesley, Mr. Lawrence    male  34.000000
# 22                         McGowan, Miss. Anna "Annie"  female  15.000000
# 23                        Sloper, Mr. William Thompson    male  28.000000
# 24                       Palsson, Miss. Torborg Danira  female   8.000000
# 25   Asplund, Mrs. Carl Oscar (Selma Augusta Emilia...  female  38.000000
# 26                             Emir, Mr. Farred Chehab    male  29.518205
# 27                      Fortune, Mr. Charles Alexander    male  19.000000
# 28                       O'Dwyer, Miss. Ellen "Nellie"  female  22.380113
# 29                                 Todoroff, Mr. Lalio    male  27.947206
# ..                                                 ...     ...        ...
# 861                        Giles, Mr. Frederick Edward    male  21.000000
# 862  Swift, Mrs. Frederick Joel (Margaret Welles Ba...  female  48.000000
# 863                  Sage, Miss. Dorothy Edith "Dolly"  female  10.869867
# 864                             Gill, Mr. John William    male  24.000000
# 865                           Bystrom, Mrs. (Karolina)  female  42.000000
# 866                       Duran y More, Miss. Asuncion  female  27.000000
# 867               Roebling, Mr. Washington Augustus II    male  31.000000
# 868                        van Melkebeke, Mr. Philemon    male  25.977889
# 869                    Johnson, Master. Harold Theodor    male   4.000000
# 870                                  Balkic, Mr. Cerin    male  26.000000
# 871   Beckwith, Mrs. Richard Leonard (Sallie Monypeny)  female  47.000000
# 872                           Carlsson, Mr. Frans Olof    male  33.000000
# 873                        Vander Cruyssen, Mr. Victor    male  47.000000
# 874              Abelson, Mrs. Samuel (Hannah Wizosky)  female  28.000000
# 875                   Najib, Miss. Adele Kiamie "Jane"  female  15.000000
# 876                      Gustafsson, Mr. Alfred Ossian    male  20.000000
# 877                               Petroff, Mr. Nedelio    male  19.000000
# 878                                 Laleff, Mr. Kristo    male  27.947206
# 879      Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)  female  56.000000
# 880       Shelley, Mrs. William (Imanita Parrish Hall)  female  25.000000
# 881                                 Markun, Mr. Johann    male  33.000000
# 882                       Dahlberg, Miss. Gerda Ulrika  female  22.000000
# 883                      Banfield, Mr. Frederick James    male  28.000000
# 884                             Sutehall, Mr. Henry Jr    male  25.000000
# 885               Rice, Mrs. William (Margaret Norton)  female  39.000000
# 886                              Montvila, Rev. Juozas    male  27.000000
# 887                       Graham, Miss. Margaret Edith  female  19.000000
# 888           Johnston, Miss. Catherine Helen "Carrie"  female  16.127950
# 889                              Behr, Mr. Karl Howell    male  26.000000
# 890                                Dooley, Mr. Patrick    male  32.000000
#
#      SibSp  Parch            Ticket      Fare Cabin Embarked
# 0        1      0         A/5 21171    7.2500    No        S
# 1        1      0          PC 17599   71.2833   Yes        C
# 2        0      0  STON/O2. 3101282    7.9250    No        S
# 3        1      0            113803   53.1000   Yes        S
# 4        0      0            373450    8.0500    No        S
# 5        0      0            330877    8.4583    No        Q
# 6        0      0             17463   51.8625   Yes        S
# 7        3      1            349909   21.0750    No        S
# 8        0      2            347742   11.1333    No        S
# 9        1      0            237736   30.0708    No        C
# 10       1      1           PP 9549   16.7000   Yes        S
# 11       0      0            113783   26.5500   Yes        S
# 12       0      0         A/5. 2151    8.0500    No        S
# 13       1      5            347082   31.2750    No        S
# 14       0      0            350406    7.8542    No        S
# 15       0      0            248706   16.0000    No        S
# 16       4      1            382652   29.1250    No        Q
# 17       0      0            244373   13.0000    No        S
# 18       1      0            345763   18.0000    No        S
# 19       0      0              2649    7.2250    No        C
# 20       0      0            239865   26.0000    No        S
# 21       0      0            248698   13.0000   Yes        S
# 22       0      0            330923    8.0292    No        Q
# 23       0      0            113788   35.5000   Yes        S
# 24       3      1            349909   21.0750    No        S
# 25       1      5            347077   31.3875    No        S
# 26       0      0              2631    7.2250    No        C
# 27       3      2             19950  263.0000   Yes        S
# 28       0      0            330959    7.8792    No        Q
# 29       0      0            349216    7.8958    No        S
# ..     ...    ...               ...       ...   ...      ...
# 861      1      0             28134   11.5000    No        S
# 862      0      0             17466   25.9292   Yes        S
# 863      8      2          CA. 2343   69.5500    No        S
# 864      0      0            233866   13.0000    No        S
# 865      0      0            236852   13.0000    No        S
# 866      1      0     SC/PARIS 2149   13.8583    No        C
# 867      0      0          PC 17590   50.4958   Yes        S
# 868      0      0            345777    9.5000    No        S
# 869      1      1            347742   11.1333    No        S
# 870      0      0            349248    7.8958    No        S
# 871      1      1             11751   52.5542   Yes        S
# 872      0      0               695    5.0000   Yes        S
# 873      0      0            345765    9.0000    No        S
# 874      1      0         P/PP 3381   24.0000    No        C
# 875      0      0              2667    7.2250    No        C
# 876      0      0              7534    9.8458    No        S
# 877      0      0            349212    7.8958    No        S
# 878      0      0            349217    7.8958    No        S
# 879      0      1             11767   83.1583   Yes        C
# 880      0      1            230433   26.0000    No        S
# 881      0      0            349257    7.8958    No        S
# 882      0      0              7552   10.5167    No        S
# 883      0      0  C.A./SOTON 34068   10.5000    No        S
# 884      0      0   SOTON/OQ 392076    7.0500    No        S
# 885      0      5            382652   29.1250    No        Q
# 886      0      0            211536   13.0000    No        S
# 887      0      0            112053   30.0000   Yes        S
# 888      1      2        W./C. 6607   23.4500    No        S
# 889      0      0            111369   30.0000   Yes        C
# 890      0      0            370376    7.7500    No        Q
#
# [891 rows x 12 columns]
dummies_Cabin = pd.get_dummies(data_train['Cabin'], prefix= 'Cabin')
dummies_Embarked = pd.get_dummies(data_train['Embarked'], prefix= 'Embarked')
dummies_Sex = pd.get_dummies(data_train['Sex'], prefix= 'Sex')
dummies_Pclass = pd.get_dummies(data_train['Pclass'], prefix= 'Pclass')
df = pd.concat([data_train, dummies_Cabin, dummies_Embarked, dummies_Sex, dummies_Pclass], axis=1)
df.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)
# print df
#      PassengerId  Survived        Age  SibSp  Parch      Fare  Cabin_No  \
# 0              1         0  22.000000      1      0    7.2500         1
# 1              2         1  38.000000      1      0   71.2833         0
# 2              3         1  26.000000      0      0    7.9250         1
# 3              4         1  35.000000      1      0   53.1000         0
# 4              5         0  35.000000      0      0    8.0500         1
# 5              6         0  23.828953      0      0    8.4583         1
# 6              7         0  54.000000      0      0   51.8625         0
# 7              8         0   2.000000      3      1   21.0750         1
# 8              9         1  27.000000      0      2   11.1333         1
# 9             10         1  14.000000      1      0   30.0708         1
# 10            11         1   4.000000      1      1   16.7000         0
# 11            12         1  58.000000      0      0   26.5500         0
# 12            13         0  20.000000      0      0    8.0500         1
# 13            14         0  39.000000      1      5   31.2750         1
# 14            15         0  14.000000      0      0    7.8542         1
# 15            16         1  55.000000      0      0   16.0000         1
# 16            17         0   2.000000      4      1   29.1250         1
# 17            18         1  32.066493      0      0   13.0000         1
# 18            19         0  31.000000      1      0   18.0000         1
# 19            20         1  29.518205      0      0    7.2250         1
# 20            21         0  35.000000      0      0   26.0000         1
# 21            22         1  34.000000      0      0   13.0000         0
# 22            23         1  15.000000      0      0    8.0292         1
# 23            24         1  28.000000      0      0   35.5000         0
# 24            25         0   8.000000      3      1   21.0750         1
# 25            26         1  38.000000      1      5   31.3875         1
# 26            27         0  29.518205      0      0    7.2250         1
# 27            28         0  19.000000      3      2  263.0000         0
# 28            29         1  22.380113      0      0    7.8792         1
# 29            30         0  27.947206      0      0    7.8958         1
# ..           ...       ...        ...    ...    ...       ...       ...
# 861          862         0  21.000000      1      0   11.5000         1
# 862          863         1  48.000000      0      0   25.9292         0
# 863          864         0  10.869867      8      2   69.5500         1
# 864          865         0  24.000000      0      0   13.0000         1
# 865          866         1  42.000000      0      0   13.0000         1
# 866          867         1  27.000000      1      0   13.8583         1
# 867          868         0  31.000000      0      0   50.4958         0
# 868          869         0  25.977889      0      0    9.5000         1
# 869          870         1   4.000000      1      1   11.1333         1
# 870          871         0  26.000000      0      0    7.8958         1
# 871          872         1  47.000000      1      1   52.5542         0
# 872          873         0  33.000000      0      0    5.0000         0
# 873          874         0  47.000000      0      0    9.0000         1
# 874          875         1  28.000000      1      0   24.0000         1
# 875          876         1  15.000000      0      0    7.2250         1
# 876          877         0  20.000000      0      0    9.8458         1
# 877          878         0  19.000000      0      0    7.8958         1
# 878          879         0  27.947206      0      0    7.8958         1
# 879          880         1  56.000000      0      1   83.1583         0
# 880          881         1  25.000000      0      1   26.0000         1
# 881          882         0  33.000000      0      0    7.8958         1
# 882          883         0  22.000000      0      0   10.5167         1
# 883          884         0  28.000000      0      0   10.5000         1
# 884          885         0  25.000000      0      0    7.0500         1
# 885          886         0  39.000000      0      5   29.1250         1
# 886          887         0  27.000000      0      0   13.0000         1
# 887          888         1  19.000000      0      0   30.0000         0
# 888          889         0  16.127950      1      2   23.4500         1
# 889          890         1  26.000000      0      0   30.0000         0
# 890          891         0  32.000000      0      0    7.7500         1
#
#      Cabin_Yes  Embarked_C  Embarked_Q  Embarked_S  Sex_female  Sex_male  \
# 0            0           0           0           1           0         1
# 1            1           1           0           0           1         0
# 2            0           0           0           1           1         0
# 3            1           0           0           1           1         0
# 4            0           0           0           1           0         1
# 5            0           0           1           0           0         1
# 6            1           0           0           1           0         1
# 7            0           0           0           1           0         1
# 8            0           0           0           1           1         0
# 9            0           1           0           0           1         0
# 10           1           0           0           1           1         0
# 11           1           0           0           1           1         0
# 12           0           0           0           1           0         1
# 13           0           0           0           1           0         1
# 14           0           0           0           1           1         0
# 15           0           0           0           1           1         0
# 16           0           0           1           0           0         1
# 17           0           0           0           1           0         1
# 18           0           0           0           1           1         0
# 19           0           1           0           0           1         0
# 20           0           0           0           1           0         1
# 21           1           0           0           1           0         1
# 22           0           0           1           0           1         0
# 23           1           0           0           1           0         1
# 24           0           0           0           1           1         0
# 25           0           0           0           1           1         0
# 26           0           1           0           0           0         1
# 27           1           0           0           1           0         1
# 28           0           0           1           0           1         0
# 29           0           0           0           1           0         1
# ..         ...         ...         ...         ...         ...       ...
# 861          0           0           0           1           0         1
# 862          1           0           0           1           1         0
# 863          0           0           0           1           1         0
# 864          0           0           0           1           0         1
# 865          0           0           0           1           1         0
# 866          0           1           0           0           1         0
# 867          1           0           0           1           0         1
# 868          0           0           0           1           0         1
# 869          0           0           0           1           0         1
# 870          0           0           0           1           0         1
# 871          1           0           0           1           1         0
# 872          1           0           0           1           0         1
# 873          0           0           0           1           0         1
# 874          0           1           0           0           1         0
# 875          0           1           0           0           1         0
# 876          0           0           0           1           0         1
# 877          0           0           0           1           0         1
# 878          0           0           0           1           0         1
# 879          1           1           0           0           1         0
# 880          0           0           0           1           1         0
# 881          0           0           0           1           0         1
# 882          0           0           0           1           1         0
# 883          0           0           0           1           0         1
# 884          0           0           0           1           0         1
# 885          0           0           1           0           1         0
# 886          0           0           0           1           0         1
# 887          1           0           0           1           1         0
# 888          0           0           0           1           1         0
# 889          1           1           0           0           0         1
# 890          0           0           1           0           0         1
#
#      Pclass_1  Pclass_2  Pclass_3
# 0           0         0         1
# 1           1         0         0
# 2           0         0         1
# 3           1         0         0
# 4           0         0         1
# 5           0         0         1
# 6           1         0         0
# 7           0         0         1
# 8           0         0         1
# 9           0         1         0
# 10          0         0         1
# 11          1         0         0
# 12          0         0         1
# 13          0         0         1
# 14          0         0         1
# 15          0         1         0
# 16          0         0         1
# 17          0         1         0
# 18          0         0         1
# 19          0         0         1
# 20          0         1         0
# 21          0         1         0
# 22          0         0         1
# 23          1         0         0
# 24          0         0         1
# 25          0         0         1
# 26          0         0         1
# 27          1         0         0
# 28          0         0         1
# 29          0         0         1
# ..        ...       ...       ...
# 861         0         1         0
# 862         1         0         0
# 863         0         0         1
# 864         0         1         0
# 865         0         1         0
# 866         0         1         0
# 867         1         0         0
# 868         0         0         1
# 869         0         0         1
# 870         0         0         1
# 871         1         0         0
# 872         1         0         0
# 873         0         0         1
# 874         0         1         0
# 875         0         0         1
# 876         0         0         1
# 877         0         0         1
# 878         0         0         1
# 879         1         0         0
# 880         0         1         0
# 881         0         0         1
# 882         0         0         1
# 883         0         1         0
# 884         0         0         1
# 885         0         0         1
# 886         0         1         0
# 887         1         0         0
# 888         0         0         1
# 889         1         0         0
# 890         0         0         1
#
# [891 rows x 16 columns]

scaler = preprocessing.StandardScaler()
age_scale_param = scaler.fit(df['Age'])
df['Age_scaled'] = scaler.fit_transform(df['Age'], age_scale_param)
fare_scale_param = scaler.fit(df['Fare'])
df['Fare_scaled'] = scaler.fit_transform(df['Fare'], fare_scale_param)


from sklearn import linear_model

# 用正则取出我们要的属性值
train_df = df.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
train_np = train_df.as_matrix()

# y即Survival结果
y = train_np[:, 0]

# X即特征属性值
X = train_np[:, 1:]

# fit到RandomForestRegressor之中
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
clf.fit(X, y)

# LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
#           intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
#           penalty='l1', random_state=None, solver='liblinear', tol=1e-06,
#           verbose=0, warm_start=False)

data_test = pd.read_csv("test.csv")
data_test.loc[ (data_test.Fare.isnull()), 'Fare' ] = 0
# 接着我们对test_data做和train_data中一致的特征变换
# 首先用同样的RandomForestRegressor模型填上丢失的年龄
tmp_df = data_test[['Age','Fare', 'Parch', 'SibSp', 'Pclass']]
null_age = tmp_df[data_test.Age.isnull()].as_matrix()
# 根据特征属性X预测年龄并补上
X = null_age[:, 1:]
predictedAges = rfr.predict(X)
data_test.loc[ (data_test.Age.isnull()), 'Age' ] = predictedAges

data_test = set_Cabin_type(data_test)
dummies_Cabin = pd.get_dummies(data_test['Cabin'], prefix= 'Cabin')
dummies_Embarked = pd.get_dummies(data_test['Embarked'], prefix= 'Embarked')
dummies_Sex = pd.get_dummies(data_test['Sex'], prefix= 'Sex')
dummies_Pclass = pd.get_dummies(data_test['Pclass'], prefix= 'Pclass')


df_test = pd.concat([data_test, dummies_Cabin, dummies_Embarked, dummies_Sex, dummies_Pclass], axis=1)
df_test.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)
df_test['Age_scaled'] = scaler.fit_transform(df_test['Age'], age_scale_param)
df_test['Fare_scaled'] = scaler.fit_transform(df_test['Fare'], fare_scale_param)


test = df_test.filter(regex='Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
predictions = clf.predict(test)
result = pd.DataFrame({'PassengerId':data_test['PassengerId'].as_matrix(), 'Survived':predictions.astype(np.int32)})
result.to_csv("logistic_regression_predictions.csv", index=False)