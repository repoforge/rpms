# $Id$
# Authority: shuff
# Upstream: Jose Luis Martinez <jlmartinez$capside,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Opsview-StatusAPI

Summary: Module to help you query the Opsview Status API
Name: perl-Opsview-StatusAPI
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Opsview-StatusAPI/

Source: http://search.cpan.org/CPAN/authors/id/J/JL/JLMARTIN/Opsview-StatusAPI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(JSON::Any)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Simple)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(HTTP::Request)
Requires: perl(JSON::Any)
Requires: perl(LWP::UserAgent)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module queries the Opsview Status API for you, returning data structures
as appropiate.

Documentation of the Status API is here:
http://docs.opsview.com/doku.php?id=opsview-community:api

Note: this module only queries the "status API", it doesn't understand about
the API to create/delete objects

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc META.yml 
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Opsview/StatusAPI.pm
#%{perl_vendorlib}/Opsview/StatusAPI/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Oct 15 2010 Steve Huff <shuff@vecna.org> - 0.01
- Initial package.
