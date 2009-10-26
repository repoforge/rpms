# $Id$
# Authority: cmr
# Upstream: Vincent Pit <perl$profvince,com>

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

%define real_name Variable-Magic

Summary: Associate user-defined magic to variables from Perl
Name: perl-Variable-Magic
Version: 0.38
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Variable-Magic/

Source: http://www.cpan.org/modules/by-module/Variable/Variable-Magic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More)   conflicts with perl package
BuildRequires: perl(XSLoader)
#BuildRequires: perl(base)  conflicts with perl package
BuildRequires: perl >= 5.008
Requires: perl(Carp)
Requires: perl(Exporter)
Requires: perl(XSLoader)
#Requires: perl(base)  conflicts with perl package
Requires: perl >= 5.008

%filter_from_requires /^perl*/d
%filter_setup

%description
Associate user-defined magic to variables from Perl.

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

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README samples/
%doc %{_mandir}/man3/Variable::Magic.3pm*
%dir %{perl_vendorarch}/auto/Variable/
%{perl_vendorarch}/auto/Variable/Magic/
%dir %{perl_vendorarch}/Variable/
%{perl_vendorarch}/Variable/Magic.pm

%changelog
* Fri Oct 16 2009 Christoph Maser <cmr@financial.com> - 0.38-1
- Updated to version 0.38.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.37-1
- Updated to version 0.37.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 0.36-1
- Updated to version 0.36.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.35-1
- Initial package. (using DAR)
