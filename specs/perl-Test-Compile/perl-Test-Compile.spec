# $Id$
# Authority: dag
# Upstream: Marcel Grënauer <marcel$cpan,org>

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

%define real_name Test-Compile

Summary: check whether Perl module files compile correctly
Name: perl-Test-Compile
Version: 0.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Compile/

Source: http://www.cpan.org/modules/by-module/Test/Test-Compile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Devel::CheckOS) >= 1.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl >= 5.6.0
Requires: perl(Devel::CheckOS) >= 1.42
Requires: perl(UNIVERSAL::require)
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup

%description
check whether Perl module files compile correctly.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Test::Compile.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Compile/
%{perl_vendorlib}/Test/Compile.pm

%changelog
* Thu Oct 22 2009 Christoph Maser <cmr@financial.com> - 0.10-1
- Updated to version 0.10.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
