# $Id$
# Authority: shuff
# Upstream: Steve Huff <shuff$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-NotifyMyAndroid

Summary: Perl interface to Notify My Android web API
Name: perl-WebService-NotifyMyAndroid
Version: 0.0.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-NotifyMyAndroid/

Source: http://search.cpan.org/CPAN/authors/id/S/SH/SHUFF/WebService-NotifyMyAndroid-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(Module::Build) >= 0.36
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Readonly)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Perl::Critic)
BuildRequires: perl(Test::Pod) >= 1.14
BuildRequires: perl(Test::Pod::Coverage) >= 1.04
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

Conflicts: perl-WebService-NMA
Obsoletes: perl-WebService-NMA

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
WebService::NotifyMyAndroid is a Perl interface to the Notify My Android
(https://nma.usk.bz/) web API. One or more NotifyMyAndroid API keys are
necessary in order to use this module.

%prep
%setup -n %{real_name}-v%{version}

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
%{perl_vendorlib}/WebService/NotifyMyAndroid.pm
#%{perl_vendorlib}/WebService/NotifyMyAndroid/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jul 06 2011 Steve Huff <shuff@vecna.org> - 0.0.2-1
- Changed name to perl-WebService-NotifyMyAndroid.
- Updated version to 0.0.2.

* Mon Jun 27 2011 Steve Huff <shuff@vecna.org> - 0.0.1-1
- Initial package.
