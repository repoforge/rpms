# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk$cpan,org>

### EL6 ships with perl-YAML-Tiny-1.40-2.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-Tiny

Summary: Read/Write YAML files with as little code as possible
Name: perl-YAML-Tiny
Version: 1.48
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-Tiny/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/YAML-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(YAML) >= 0.72
BuildRequires: perl(YAML::Perl) >= 0.02
BuildRequires: perl(YAML::Syck) >= 1.17
BuildRequires: perl(YAML::XS) >= 0.34
BuildRequires: perl >= 5.004
Requires: perl >= 5.004

%filter_from_requires /^perl*/d
%filter_setup

%description
Read/Write YAML files with as little code as possible.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/YAML::Tiny.3pm*
%dir %{perl_vendorlib}/YAML/
#%{perl_vendorlib}/YAML/Tiny/
%{perl_vendorlib}/YAML/Tiny.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.48-1
- Updated to version 1.48.

* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 1.41-1
- Updated to version 1.41.

* Mon Aug  3 2009 Christoph Maser <cmr@financial.com> - 1.40-1
- Updated to version 1.40.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 1.39-1
- Updated to version 1.39.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.31-1
- Updated to release 1.31.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.25-1
- Updated to release 1.25.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 1.21-1
- Updated to release 1.21.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.19-1
- Updated to release 1.19.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
