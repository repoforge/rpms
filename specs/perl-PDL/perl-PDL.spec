# $Id$
# Authority: dag
# Upstream: Chris Marshall <chm$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PDL

Summary: Perl module that implements the Perl Data Language
Name: perl-PDL
Version: 2.4.4
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PDL/

Source: http://www.cpan.org/modules/by-module/PDL/PDL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-PDL is a Perl module that implements the Perl Data Language.

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
%doc BUGS COPYING Changes INSTALL MANIFEST MANIFEST.SKIP META.yml README Release_Notes TODO
%doc %{_mandir}/man1/PDL::*.1*
%doc %{_mandir}/man1/pdl.1*
%doc %{_mandir}/man1/pdldoc.1*
%doc %{_mandir}/man1/perldl.1*
%doc %{_mandir}/man1/pptemplate.1*
%doc %{_mandir}/man3/PDL.3pm*
%doc %{_mandir}/man3/PDL::*.3pm*
%doc %{_mandir}/man3/Pdlpp.3pm*
%{_bindir}/pdl
%{_bindir}/pdldoc
%{_bindir}/perldl
%{_bindir}/pptemplate
%{perl_vendorarch}/auto/PDL/
%dir %{perl_vendorarch}/Inline/
%{perl_vendorarch}/Inline/MakePdlppInstallable.pm
%{perl_vendorarch}/Inline/Pdlpp.pm
%{perl_vendorarch}/PDL/
%{perl_vendorarch}/PDL.pm

%changelog
* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 2.4.4-1
- Updated to release 2.4.4.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 2.4.3-1
- Initial package. (using DAR)
