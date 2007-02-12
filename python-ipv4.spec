
%define 	module	ipv4

Summary:	IPv4 Utils - A module that helps dealing with IPv4 networks, hosts and other concepts
Summary(pl.UTF-8):   IPv4 - moduł pomagający w obsłudze sieci, hostów i innych aspektów IPv4
Name:		python-%{module}
Version:	0.35
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.sil-tec.gr/~tzot/python/IPv4_Utils-0.35.linux-i586.tar.gz
# Source0-md5:	174c80f2556f6f74ca8c0990a30d6afa
URL:		http://www.sil-tec.gr/~tzot/python/
%pyrequires_eq 	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A module that helps dealing with IPv4 networks, hosts and other
concepts.

%description -l pl.UTF-8
Moduł pomagający w obsłudze sieci, hostów i innych aspektów IPv4.

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
