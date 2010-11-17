# $Id$
# Authority: dries
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

### EL6 ships with perl-MIME-Lite-3.027-2.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-Lite

Summary: Simple standalone module for generating MIME messages
Name: perl-MIME-Lite
Version: 3.027
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-Lite/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/MIME-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Email::Date::Format) >= 1.000
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
Requires: perl(Email::Date::Format) >= 1.000
Requires: perl(File::Spec)

%filter_from_requires /^perl*/d
%filter_setup

%description
MIME-Lite is a simple standalone module for generating MIME messages.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find contrib/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALLING LICENSE MANIFEST META.yml README changes.pod contrib/ examples/
%doc %{_mandir}/man3/MIME::Lite.3pm*
%doc %{_mandir}/man3/MIME::changes.3pm*
%dir %{perl_vendorlib}/MIME/
#%{perl_vendorlib}/MIME/Lite/
%{perl_vendorlib}/MIME/Lite.pm
%{perl_vendorlib}/MIME/changes.pod

%changelog
* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 3.027-1
- Updated to version 3.027.

* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 3.025-1
- Updated to version 3.025.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 3.024-1
- Updated to version 3.024.

* Fri Jan 16 2009 Christoph Maser <cmr@financial.com> - 3.023-1
- Updated to release 3.023.
- Add dependency for perl(Email::Date::Format)

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 3.021-1
- Updated to release 3.021.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 3.020-1
- Updated to release 3.020.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> 3.01-2
- URL changed to cpan.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> 3.01-1
- Updated to release 3.01.

* Sun Dec 11 2004 Dries Verachtert <dries@ulyssis.org> 2.117-2
- cleanup of spec file

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 2.117-1
- first packaging for Fedora Core 1
