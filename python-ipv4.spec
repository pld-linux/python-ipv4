
%define 	module	ipv4

Summary:	IPv4 Utils - A module that helps dealing with IPv4 networks, hosts and other concepts
Name:		python-%{module}
Version:	0.35
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.sil-tec.gr/~tzot/python/IPv4_Utils-0.35.linux-i586.tar.gz
# Source0-md5:	174c80f2556f6f74ca8c0990a30d6afa
URL:		http://www.sil-tec.gr/~tzot/python/
BuildArch:	noarch
%pyrequires_eq 	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A module that helps dealing with IPv4 networks, hosts and other concepts.

%prep
%setup -q -n usr 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
install local/lib/python2.3/site-packages/*.py $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
