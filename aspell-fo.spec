Summary:	Faroese dictionary for aspell
Summary(fo.UTF-8):   Føroyska orðalistan til rættlestur
Summary(pl.UTF-8):   Słownik farerski dla aspella
Name:		aspell-fo
Version:	0.2.16
%define	subv	1
Release:	1
Epoch:		2
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/fo/aspell5-fo-%{version}-%{subv}.tar.bz2
# Source0-md5:	a57e8870c272931da41cd1fc5a291f3d
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Faroese dictionary (i.e. word list) for aspell.

%description -l fo.UTF-8
Føroyska orðalistan til rættlestur.

%description -l pl.UTF-8
Słownik farerski (lista słów) dla aspella.

%prep
%setup -q -n aspell5-fo-%{version}-%{subv}

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
%doc Copyright README doc/contributors
%{_libdir}/aspell/*
%{_datadir}/aspell/*
