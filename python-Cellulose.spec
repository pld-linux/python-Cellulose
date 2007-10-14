#
%define	module	Cellulose
#
Summary:	Python/Cellulose package
Summary(pl.UTF-8):	Pakiet Python/Cellulose
Name:		python-%{module}
Version:	0.2
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/C/Cellulose/%{module}-%{version}.tar.gz
# Source0-md5:	fc62bc2867fc20832b2d75e63cfd5434
URL:		http://cheeseshop.python.org/pypi/Cellulose/
BuildRequires:	python >= 1:2.4
BuildRequires:	python-setuptools
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stateful, object-oriented, pseudo-functional programming in python.

%description -l pl.UTF-8
Stanowe, zorientowane obiektowo, pseudo-funkcyjne programowanie w
języku Python.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

cp -af cellulose $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG LICENSE README TODO
%doc docs
%{py_sitescriptdir}/cellulose
