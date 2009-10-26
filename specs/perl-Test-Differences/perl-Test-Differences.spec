# $Id$
# Authority: dries
# Upstream: Barrie Slaymaker <barries$slaysys,com>

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

%define real_name Test-Differences

Summary: Test strings and data structures and show differences if not ok
Name: perl-Test-Differences
Version: 0.500
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Differences/

Source: http://www.cpan.org/modules/by-module/Test/Test-Differences-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Diff) >= 0.35
Requires: perl(Test::More)
Requires: perl(Text::Diff) >= 0.35

%filter_from_requires /^perl*/d
%filter_setup

%description
Test strings and data structures and show differences if not ok.

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
%doc Changes MANIFEST 
%doc %{_mandir}/man3/Test::Differences.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Differences/
%{perl_vendorlib}/Test/Differences.pm

%changelog
* Thu Oct 22 2009 Christoph Maser <cmr@financial.com> - 0.500-1
- Updated to version 0.500.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.4801-1
- Updated to version 0.4801.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.47-1
- Initial package.
