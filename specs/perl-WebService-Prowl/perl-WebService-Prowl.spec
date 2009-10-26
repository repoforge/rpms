# $Id$
# Authority: shuff
# Upstream: Masayoshi Sekimura <sekimura$cpan,org>

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

%define real_name WebService-Prowl

Summary: a interface to Prowl Public API
Name: perl-%{real_name}
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-Prowl/

Source: http://search.cpan.org/CPAN/authors/id/S/SE/SEKIMURA/WebService-Prowl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge

Requires: perl(XML::Simple)

### AnyEvent::HTTP is optional, not required
%filter_from_requires /^perl(AnyEvent.*/d
%filter_setup

%description
This module aims to be a implementation of a interface to the Prowl Public API
(as available on http://forums.cocoaforge.com/viewtopic.php?f=45&t=20339)

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
%doc %{_mandir}/man3/WebService::Prowl.3pm*
%doc %{_mandir}/man3/WebService::Prowl::*.3pm*
%dir %{perl_vendorlib}/WebService/
%dir %{perl_vendorlib}/WebService/Prowl/
%{perl_vendorlib}/WebService/Prowl.pm
%{perl_vendorlib}/WebService/Prowl/*.pm

%changelog
* Sat Oct 03 2009 Steve Huff <shuff@vecna.org> - 0.05-1
- Updated to version 0.05.

* Thu Oct 01 2009 Steve Huff <shuff@vecna.org> - 0.04-1
- Initial package.
