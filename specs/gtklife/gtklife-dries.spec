# $Id$

# Authority: dries

Summary: Conway's Life simulator
Name: gtklife
Version: 1.0
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.igs.net/~tril/gtklife/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.igs.net/~tril/gtklife/gtklife-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}

BuildRequires: gtk2-devel

%description
todo

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README

%changelog
* Sun Mar 21 2004 Dries Verachtert <dries@ulyssis.org> 1.0-1
- Initial package
