# $Id: $

# Authority: dries
# Upstream: 

Summary: Extension for reading and writing YAML
Name: syck
Version: 0.42
Release: 1
License: GPL
Group: Development/Libraries
URL: http://www.whytheluckystiff.net/syck/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/yaml4r/syck-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildRequires: 

%description
Syck is an extension for reading and writing YAML swiftly in popular
scripting languages. As Syck loads the YAML, it stores the data directly in
your language's symbol table.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_includedir}/*.h
%{_libdir}/*.a

%changelog
* Sat Jul 31 2004 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Initial package.
