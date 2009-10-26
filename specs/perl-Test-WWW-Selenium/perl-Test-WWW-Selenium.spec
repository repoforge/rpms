# $Id$
# Authority: dries
# Upstream: Luke Closs <cpan$5thplane,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

### BEGIN KLUDGE
## temporary fix until package builders install rpm-macros-rpmforge in their
## build environments; once that's done, remove the kludge
## 2009-10-26 shuff

# prevent anything matching from being scanned for provides
%define filter_provides_in(P) %{expand: \
%global __filter_prov_cmd %{?__filter_prov_cmd} %{__grep} -v %{-P} '%*' | \
}

# prevent anything matching from being scanned for requires
%define filter_requires_in(P) %{expand: \
%global __filter_req_cmd %{?__filter_req_cmd} %{__grep} -v %{-P} '%*' | \
}

# filter anything matching out of the provides stream
%define filter_from_provides() %{expand: \
%global __filter_from_prov %{?__filter_from_prov} | %{__sed} -e '%*' \
}

# filter anything matching out of the requires stream
%define filter_from_requires() %{expand: \
%global __filter_from_req %{?__filter_from_req} | %{__sed} -e '%*' \
}

# actually set up the filtering bits 
%define filter_setup %{expand: \
%global _use_internal_dependency_generator 0 \
%global __deploop() while read FILE; do /usr/lib/rpm/rpmdeps -%{1} ${FILE}; done | /bin/sort -u \
%global __find_provides /bin/sh -c "%{?__filter_prov_cmd} %{__deploop P} %{?__filter_from_prov}" \
%global __find_requires /bin/sh -c "%{?__filter_req_cmd}  %{__deploop R} %{?__filter_from_req}" \
}
### END KLUDGE

%define real_name Test-WWW-Selenium

Summary: Test applications using Selenium Remote Control
Name: perl-Test-WWW-Selenium
Version: 1.19
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-WWW-Selenium/

Source: http://www.cpan.org/modules/by-module/Test/Test-WWW-Selenium-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Mock::LWP)
#BuildRequires: perl(Test::More) >= 0.42 
BuildRequires: perl(Test::Pod)
BuildRequires: perl(URI::Escape) >= 1.31
Requires: perl(LWP::UserAgent)
Requires: perl(URI::Escape) >= 1.31

%filter_from_requires /^perl*/d
%filter_setup

%description
Test applications using Selenium Remote Control.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc Changes README todo.txt
%doc %{_mandir}/man3/Test::WWW::Selenium.3pm*
%doc %{_mandir}/man3/WWW::Selenium.3pm*
%doc %{_mandir}/man3/WWW::Selenium::Util.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/WWW/
%{perl_vendorlib}/Test/WWW/Selenium.pm
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Selenium.pm
%{perl_vendorlib}/WWW/Selenium/Util.pm
%{perl_vendorlib}/Test/WWW/mypod2html.pl

%changelog
* Fri Oct 16 2009 Christoph Maser <cmr@financial.com> - 1.19-1
- Updated to version 1.19.

* Fri Sep  4 2009 Christoph Maser <cmr@financial.com> - 1.18-1
- Updated to version 1.18.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.17-1
- Updated to version 1.17.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Initial package.
