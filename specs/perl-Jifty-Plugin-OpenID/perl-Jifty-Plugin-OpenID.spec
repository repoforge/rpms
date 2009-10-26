# $Id$
# Authority: shuff
# Upstream: Yves Agostini <agostini$univ-metz,fr>

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

%define real_name Jifty-Plugin-OpenID

Summary: Provides OpenID authentication for your jifty app
Name: perl-%{real_name}
Version: 1.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jifty-Plugin-OpenID/

Source: http://search.cpan.org/CPAN/authors/id/Y/YV/YVESAGO/Jifty-Plugin-OpenID-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Cache::FileCache)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Jifty)
BuildRequires: perl(LWPx::ParanoidAgent)
BuildRequires: perl(Net::OpenID::Consumer)
# BuildRequires: rpm-macros-rpmforge

# we don't want to either provide or require anything from _docdir, per policy
%filter_provides_in %{_docdir}
%filter_requires_in %{_docdir}

%filter_from_requires /^perl(Jifty::Plugin::OpenID.*/d
%filter_setup

%description
OpenID authentication for Jifty applications.

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
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Jifty/Plugin/
%{perl_vendorlib}/Jifty/Plugin/*


%changelog
* Mon Oct 05 2009 Steve Huff <shuff@vecna.org> - 1.00-1
- Initial package.

