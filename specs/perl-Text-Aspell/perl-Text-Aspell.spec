# $Id$
# Authority: dag
# Upstream: Bill Moseley <mods$hank,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Aspell

Summary: Perl module to the GNU Aspell library
Name: perl-Text-Aspell
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Aspell/

Source: http://www.cpan.org/modules/by-module/Text/Text-Aspell-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Text-Aspell is a Perl module to the GNU Aspell library.

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
%doc %{_mandir}/man3/Text::Aspell.3pm*
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/Aspell/
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/Aspell.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
