# Description of the repository

This python module has been developed to determine the glass optic properties. Data sets are extracted from Interglad V8 and SciGlass databases. Artificial Neural Networks are fitted using keras library.

# Requirements

Python modules involved in this module are:

- `numpy`
- `pandas`
- `matplotlib`
- `molmass`
- `seaborn`
- `sklearn`
- `tensorflow`


# Repository constitution

Under this repository, various files are provided. The list is the following:

- `glassdata.py`
- `network.py`
- `pretreatmentdatabase.py'
- 'sciglassextraction.py'
- 'sciglasstodatabase.py'
- `glassproperties.py`
- `nntrainingproperty.py`

## `glassdata.py`

`glassdata.py` file defines the GlassData class. It gathers various functions to
clean datasets and manages data for the training stage. It is composed by the
following variables

-   `oxide`: Array of string
    Names of the oxides of the glass composition.
-   `nameproperty`: String
    Name of the property of the glasses.
-   `nsample`: Integer
    Number of the glass.
-   `noxide`: Integer
    Number of oxides constituting the glass composition.
-   `nbO`: Array of integer of the noxide oxides
    number of oxygen in each oxide.
-   `cation`: Array of string of the noxide oxides
    name of the cation in each oxide.
-   `nbcation`: Array of integer of the noxide oxides
    number of cation in each oxide.
-   `Moxide`: Array of float of the noxide oxides
    molar mass of each oxide.
-   `x`: Array of float (nsample,noxide)
    Molar fraction of the noxide oxides of the nsample glass composition.
-   `y`: Array of float of the nsample glass composition.
    Property of glass of the data set.
-   `xmin`: Array of float of the noxide oxides
    Minimum of the molar fraction of each oxide (=0)
-   `xmax`: Array of float of the noxide oxides
    Maximum of the molar fraction of each oxide in the data set.
-   `occurence`: Array of integer
    Numbers of composition for which the molar fraction of each oxide is stricly different to zero.
-   `MolarM`: Array of float of  the nsample glass composition.
    Molar mass of each glass composition in kg/mol.

The methods associated to this GlassData class are:

-   `load(self,filename)`: Loading of dataset from csv file called filename.
-   `info(self)`: Print information about dataset.
-   `shape(self)`: Return shape of input dataset.
-   `oxidemolarmass(self)`: Molar mass of each oxide in kg/mol.
-   `molarmass(self)`: Molar mass for each glass.
-   `bounds(self)`: Determination of the minimum, maximum and occurence of each oxide.
-   `normalize_x(self)`: Normalize of x dataset.
-   `normalize_y(self)`: Normalize of y dataset.
-   `split(self,train,valid)`: Define split indices into training, validation and test sub-sets.
-   `physicalx(self,x)`: Computational of x from the norlaized values.
-   `physicaly(self,y)`: Computational of y from the norlaized values.
-   `savedata(self,filesavedata,listtodrop=None)`: Saving of the data set in a csv file with a removal of a list of samples if it exists.
-   `xglasstoxdb(self,oxide,xglass)`: Copy the array of the glass composition xglass with a list of oxide in the formatted array of the dataset.
-   `datacleaning(self,filename,xtotal,probamin,probamax,xminor,minoxidefraction,filteringoxide,Plot)`: Cleaning of the dataset gathered in the filename extracted from Interglad. Here, all unexpected characters and lines are removed. Alphanumeric characters are transformed into float.
-   `FilteringProperty(self,probamin,probamax,Plot)`: Cleaning of database by keeping glass samples for which the probability of occurrence is in tha range `[probamin,probamax]`.
-   `FilteringOxide(self,probamin,probamax,ioxide,Plot)`: Cleaning of database by keeping glass samples for which the probability of occurrence of oxide ioxide is in the range `[probamin,probamax]`.
-   `pdfoxide(self,ioxide,density,Plot,filename)`: Determination of the pdf of the oxide[ioxide].
-   `familyrandomcomposition(self,Nglass,I,J,xmol0,dx0)`: Determination of random composition of Nglass composition centered on a composition constituted of a list I of a sub-set oxides with centered composition xmol0.
-   `randomcomposition(self,Nglass,xmax)`: Determination of random composition of Nglass composition.
-   `GlassDensity(self,nnmodel,oxide,x)`: Determination of the glass density from the molar volume.
-   `YoungModulus(self,nnmodel,datadisso,oxide,x)`: Determination of the Young's modulus as a function of a composition of glass with the list of oxide and molar composition x.

## `network.py`

`network.py` is a class used to define, compile, fit an ANN model. The parameters of this class are:

-   `shape`: Integers corresponding of the number of features (= number of oxides) and number of samples in the data-set.
-   `arch`: Array defining the number of layers and each associated neurals.
-   `actv`: Activation function of hidden layers in ANN model.
-   `final`: Function of the output layer.
-   `k_init`: Kernel of initialization of parameters of the ANN.
-   `history`: Information about the fitting of the ANN.
-   `namearch`: Name of architecture used to save and call a model.

The methods associated to this are:

-   `build(self,shape,arch,actv,final)`: Build model.
-   `compile(self, lr=1.0e-3)`: Compile model.
-   `info(self)`: Print infos about model.
-   `fit(self,x_train,y_train,x_val,y_val,epochs,batch_size)`: Fitting model on data.
-   `plot(self,outputfile`'loss.png',savefig=False)=: Plot accuracy and loss.
-   `save(self, filename)`: Save model to file
-   `load(self,filename)`: Load model from file
-   `ArchName(self,arch)`: Name summarizing the architecture of the model.

## 'pretreatmentdatabase.py'

This script is used to created a data set from a csv file saved from Interglad V8.

    filename : String
        Name of the database built from the database Interglad V8.
    xtotal : Float
        Bound admited in the sum of oxides for each glass sample.
    probamin : Float
        Minimum of the probability of occurence of oxide or proprety.
    probamax : Float
        Maximum of the probability of occurence of oxide or proprety.
    xminor : Float
        Minimum value of the oxide to be considered to be significant.
    minoxidefraction : Float
        Minimum fraction of glasses with a specific oxide in the composition
    Plot : Boolean
        Parameter giving the choice to plot the pdf of the property.

## datasetstatitics.py

This script determines the probability density function of a property, the list of oxides with the number of occurences in the data-set and the maximum of molar fraction of each oxides. All these information are plotted in figures saved in a directory Figures.

## `nntrainingproperty.py`

This script is an example achieving the training of an ANN model using our own GlassData and NeuralNetwork classes.


# Data sets

Data sets for the various properties are gathered under the directory `DataSet`.

The list of data sets are the following:

-   `nC.csv`: File giving the refractive index nC after cleaning.
-   `nCInterglad.csv`: File giving the refractive index nC extracted from Interglad V8.
-   `nd.csv`: File giving the refractive index nd after cleaning.
-   `ndInterglad.csv`: File giving the refractive index nd extracted from Interglad V8.
-   `nF.csv`: File giving refractive index nF after cleaning.
-   `nFInterglad.csv`: File giving the refractive index nF extracted from Interglad V8.

# Trained ANN models

Models of artifial neural networks used to predict properties has been previously trained. They are under the directory `Models`.

-   `nnnd3c30.keras`: ANN of 3 layers of 30 neurals determined the refractive index nd.

