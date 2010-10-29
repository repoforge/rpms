# $Id$
# Authority: cmr
# Upstream: Hans Dieter Pearcey <hdp$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt-Long-Descriptive

Summary: Getopt::Long with usage text
Name: perl-Getopt-Long-Descriptive
Version: 0.086
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-Long-Descriptive/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Getopt-Long-Descriptive-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Getopt::Long) >= 2.33
BuildRequires: perl(List::Util)
BuildRequires: perl(Params::Validate) >= 0.74
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More)
Requires: perl(Getopt::Long) >= 2.33
Requires: perl(List::Util)
Requires: perl(Params::Validate) >= 0.74
Requires: perl(Sub::Exporter)
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup


%description
Getopt::Long with usage text.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Getopt::Long::Descriptive.3pm*
%doc %{_mandir}/man3/Getopt::Long::Descriptive::Opts.3pm*
%doc %{_mandir}/man3/Getopt::Long::Descriptive::Usage.3pm*
%dir %{perl_vendorlib}/Getopt/
%dir %{perl_vendorlib}/Getopt/Long/
%{perl_vendorlib}/Getopt/Long/Descriptive/Opts.pm
%{perl_vendorlib}/Getopt/Long/Descriptive/Usage.pm
%{perl_vendorlib}/Getopt/Long/Descriptive.pm

%changelog
* Fri Oct 29 2010 Christoph Maser <cmaser@gmx.de> - 0.086-1
- Updated to version 0.086.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.083-1
- Updated to version 0.083.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.077-1
- Updated to version 0.077.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.074-1
- Updated to version 0.074.

* Sat Jul 04 2009 Unknown - 0.074-1
- Initial package. (using DAR)
