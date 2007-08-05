# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name C

Summary: Compress-Zlib module for perl 
Name: perl-Compress-Zlib
Version: 1.33
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-Zlib/

Source: http://www.cpan.org/modules/by-module/Compress/Compress-Zlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.004, zlib-devel >= 1.0.2
Requires: perl >= 0:5.004, zlib >= 1.0.2

%description
Compress-Zlib module for perl

%prep
%setup -n %{real_name}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/*

%changelog
* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.33-0
- Updated to release 1.33.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.22-0
- Updated to release 1.22.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
