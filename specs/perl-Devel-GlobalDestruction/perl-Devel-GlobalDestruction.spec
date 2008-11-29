# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-GlobalDestruction

Summary: Expose PL_dirty, the flag which marks global destruction
Name: perl-Devel-GlobalDestruction
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-GlobalDestruction/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-GlobalDestruction-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Expose PL_dirty, the flag which marks global destruction.

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
%doc MANIFEST MANIFEST.SKIP META.yml SIGNATURE
%doc %{_mandir}/man3/Devel::GlobalDestruction.3pm*
%dir %{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/auto/Devel/GlobalDestruction/
%dir %{perl_vendorarch}/Devel/
%{perl_vendorarch}/Devel/GlobalDestruction.pm

%changelog
* Sat Nov 29 2008 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
