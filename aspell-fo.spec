Summary:	Faroese dictionary for aspell
Summary(pl):	Farerski s�ownik dla aspella
Name:		aspell-fo
Version:	0.1
%define	subv	3
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	http://aspell.sourceforge.net/%{name}-%{version}-%{subv}.tar.bz2
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell
Requires:	aspell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Faroese dictionary (i.e. word list) for aspell.

%description -l pl
Farerski s�ownik (lista s��w) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/aspell/*
%{_datadir}/aspell/*
%{_datadir}/pspell/*
