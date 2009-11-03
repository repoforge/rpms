# $Id$
# Authority: dag
# Upstream: Ian Guthrie <IGuthrie$aol,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Filesys-Df

Summary: Perl module for filesystem disk space information
Name: perl-Filesys-Df
Version: 0.92
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Filesys-Df/

Source: http://www.cpan.org/modules/by-module/Filesys/Filesys-Df-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Filesys-Df is a Perl module for filesystem disk space information.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Filesys::Df.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Filesys/
%{perl_vendorarch}/Filesys/Df.pm
%dir %{perl_vendorarch}/auto/Filesys/
%{perl_vendorarch}/auto/Filesys/Df/

%changelog
* Thu May 24 2007 Dag Wieers <dag@wieers.com> - 0.92-1
- Initial package. (using DAR)
