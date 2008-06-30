# $Id$
# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Versions-Report

Summary: Report versions of all modules in memory
Name: perl-Module-Versions-Report
Version: 1.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Versions-Report/

Source: http://www.cpan.org/modules/by-module/Module/Module-Versions-Report-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
If you add "use
Module::Versions::Report;" to a program (especially handy if your
program is one that demonstrates a bug in some module), then when the
program has finished running, you well get a report detailing the all
modules in memory, and noting the version of each (for modules that
defined a $VERSION, at least).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Module::Versions::Report.3pm*
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Versions/
#%{perl_vendorlib}/Module/Versions/Report/
%{perl_vendorlib}/Module/Versions/Report.pm

%changelog
* Wed Jun 25 2008 Dag Wieers <dag@wieers.com> - 1.05-1
- Updated to release 1.05.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Updated to release 1.03.

* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
