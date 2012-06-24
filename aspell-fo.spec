Summary:	Faroese dictionary for aspell
Summary(pl):	Farerski s�ownik dla aspella
Name:		aspell-fo
Version:	0.51
%define	subv	0
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/fo/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	5cc9168ad88ceb1b5531a5452527728b
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
