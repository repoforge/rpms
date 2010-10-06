# $Id$
# Authority: shuff
# Upstream: Steve Huff <shuff$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-Uptrack

Summary: access KSplice Uptrack web API
Name: perl-WebService-Uptrack
Version: 0.0.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-Uptrack/

Source: http://search.cpan.org/CPAN/authors/id/S/SH/SHUFF/WebService-Uptrack-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(JSON::XS)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::StrictConstructor)
BuildRequires: perl(Readonly)
BuildRequires: perl(Test::More)
BuildRequires: perl(version)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(Data::Dumper)
Requires: perl(HTTP::Request)
Requires: perl(HTTP::Response)
Requires: perl(JSON::XS)
Requires: perl(LWP::UserAgent)
Requires: perl(Moose)
Requires: perl(Moose::Util::TypeConstraints)
Requires: perl(MooseX::StrictConstructor)
Requires: perl(Readonly)
Requires: perl(version)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description

%prep
%setup -n %{real_name}-v%{version}

%build
%{__perl} Build.PL --installdirs=vendor --destdir="%{buildroot}"
%{__perl} Build
%{__perl} Build docs

%install
%{__rm} -rf %{buildroot}
%{__perl} Build pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README TODO
%doc %{_mandir}/man?/*
%{perl_vendorlib}/WebService/Uptrack.pm
#%{perl_vendorlib}/WebService/Uptrack/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Oct 05 2010 Steve Huff <shuff@vecna.org> - 0.0.1
- Initial package.
