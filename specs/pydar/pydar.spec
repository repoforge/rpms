# $Id: $

# Authority: dries

# Far from finished, not to be released :)

Summary: todo
Name: pydar
Version: 0.001
Release: 1
License: GPL
Group: Development/Tools
URL: todo

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: pydar-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}

%description
todo

%prep
%setup -q pydar

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
* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 0.001-1
- Initial package
