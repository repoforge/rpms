# $Id$
# Authority: dries
# Upstream: Makamaka Hannyaharamitu <makamaka$cpan,org>

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

%define real_name Text-CSV

Summary: comma-separated values manipulator (using XS or PurePerl)
Name: perl-Text-CSV
Version: 1.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-CSV/

Source: http://www.cpan.org/modules/by-module/Text/Text-CSV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(IO::Handle)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
Requires: perl(IO::Handle)
Requires: perl(Test::Harness)
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup


%description
Text::CSV provides facilities for the composition and decomposition of
comma-separated values.  An instance of the Text::CSV class can combine
fields into a CSV string and parse a CSV string into fields.

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
%doc %{_mandir}/man3/Text::CSV.3pm*
%doc %{_mandir}/man3/Text::CSV_PP.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/CSV/
%{perl_vendorlib}/Text/CSV.pm
%{perl_vendorlib}/Text/CSV_PP.pm

%changelog
* Thu Oct 22 2009 Christoph Maser <cmr@financial.com> - 1.15-1
- Updated to version 1.15.

* Mon Aug  3 2009 Christoph Maser <cmr@financial.com> - 1.13-1
- Updated to version 1.13.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.12-1
- Updated to version 1.12.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.05-1
- Updated to release 1.05.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Mon Feb 28 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
