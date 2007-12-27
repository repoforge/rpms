# $Id$
# Authority: dag
# Upstream: Ken Williams <KWILLIAMS$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PathTools

Summary: Tools for working with paths and file specs across platforms
Name: perl-PathTools
Version: 3.2501
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PathTools/

Source: http://www.cpan.org/authors/id/K/KW/KWILLIAMS/PathTools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(File::Path)
BuildRequires: perl(Module::Build) >= 0.19
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test)
Requires: perl >= 0:5.005

%description
Tools for working with paths and file specs across platforms.

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
%doc Changes INSTALL MANIFEST META.yml SIGNATURE
%doc %{_mandir}/man3/Cwd.3pm*
%doc %{_mandir}/man3/File::Spec.3pm*
%doc %{_mandir}/man3/File::Spec::*.3pm*
%{perl_vendorarch}/auto/Cwd/
%dir %{perl_vendorarch}/File/
%{perl_vendorarch}/Cwd.pm
%{perl_vendorarch}/File/Spec.pm
%{perl_vendorarch}/File/Spec/

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 3.2501-1
- Updated to release 3.2501.

* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 3.25-1
- Initial package. (using DAR)
