# $Id$
# Authority: shuff
# Upstream: SHEVEK <cpan$anarres,org>

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

%define real_name Mail-Karmasphere-Client

Summary: Client for Karmasphere Reputation Server
Name: perl-%{real_name}
Version: 2.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Karmasphere-Client/

Source: http://search.cpan.org/CPAN/authors/id/S/SH/SHEVEK/Mail-Karmasphere-Client-%{version}.tar.gz
Patch0: %{name}_noninteractive.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl >= 5.006
BuildRequires: perl(Convert::Bencode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(Lingua::EN::Inflect)
BuildRequires: perl(LWP)
BuildRequires: perl(Text::CSV)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Unix::Syslog)
BuildRequires: perl(YAML)
#BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.006
Requires: perl(Convert::Bencode)
Requires: perl(HTTP::Request)
Requires: perl(IO::Select)
Requires: perl(IO::Socket)
Requires: perl(Lingua::EN::Inflect)
Requires: perl(LWP)
Requires: perl(Text::CSV)
Requires: perl(Time::HiRes)
Requires: perl(Unix::Syslog)
Requires: perl(YAML)

Provides: %{_bindir}/karma-publish
Provides: %{_bindir}/karmaclient
Provides: %{_bindir}/karmad-exim
Provides: %{_bindir}/karmad-postfix

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
The Karmasphere reputation service is a real-time reputation service for
Internet identities.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

# retrieve the parser README
%{__mv} lib/Mail/Karmasphere/Parser/README README.parser

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml README README.parser
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Mail/
%dir %{perl_vendorlib}/Mail/SpamAssassin/Plugin/
%{perl_vendorlib}/Mail/Karmasphere/
%{perl_vendorlib}/Mail/SpamAssassin/Plugin/*
%{_bindir}/*

%changelog
* Thu Oct 29 2009 Steve Huff <shuff@vecna.org> - 2.18-1
- Initial package.
