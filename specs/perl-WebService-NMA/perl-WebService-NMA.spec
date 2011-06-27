# $Id$
# Authority: shuff
# Upstream: Steve Huff <shuff$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-NMA

Summary: Perl interface to Notify My Android web API
Name: perl-WebService-NMA
Version: 0.0.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-NMA/

Source: http://search.cpan.org/CPAN/authors/id/S/SH/SHUFF/WebService-NMA-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(Module::Build) >= 0.36
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Readonly)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Test::More)
BuildRequires: perl(WebService::Simple)
BuildRequires: perl(XML::Simple)
BuildRequires: perl(version)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(Params::Validate)
Requires: perl(Readonly)
Requires: perl(Regexp::Common)
Requires: perl(WebService::Simple)
Requires: perl(XML::Simple)
Requires: perl(version)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
WebService::NMA is a Perl interface to the Notify My Android
(https://nma.usk.bz/) web API. One or more NMA API keys are necessary in order
to use this module.

%prep
%setup -n %{real_name}-v%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Build.PL \
    --installdirs="vendor" \
    --prefix="%{buildroot}%{_prefix}"

%install
%{__rm} -rf %{buildroot}
./Build pure_install

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/WebService/NMA.pm
#%{perl_vendorlib}/WebService/NMA/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Jun 27 2011 Steve Huff <shuff@vecna.org> - 0.0.1-1
- Initial package.
