# $Id$
# Authority: shuff
# Upstream: Yves Rutschle

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-RTMAgent
%define rtm_version 0.5

Summary: UserAgent for the RememberTheMilk API 
Name: perl-%{real_name}
Version: 0.5
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-RTMAgent/

Source0: http://search.cpan.org/CPAN/authors/id/R/RU/RUTSCHLE/WebService-RTMAgent-%{version}.tar.gz
Source1: http://www.rutschle.net/rtm/rtm-%{rtm_version}.gz
Patch0: perl-WebService-RTMAgent_authorize.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::Simple)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Digest::MD5)
Requires: perl(LWP::UserAgent)
Requires: perl(XML::Simple)

Provides: %{_bindir}/rtm

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
WebService::RTMAgent is a Perl implementation of the rememberthemilk.com API.

%prep
%setup -n %{real_name}-%{version}
cd %{_builddir}
cd %{real_name}-%{version}
%{__gzip} -dc %{_sourcedir}/rtm-%{rtm_version}.gz > rtm
if [ $? -ne 0 ]; then
  exit $?
fi
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

# now the rtm script
%{__install} -m0755 -d %{buildroot}%{_bindir}
%{__install} -m0755 rtm %{buildroot}%{_bindir}

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README MANIFEST META.yml
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/WebService/
%{perl_vendorlib}/WebService/*
%{_bindir}/*

%changelog
* Mon Mar 01 2010 Steve Huff <shuff@vecna.org> - 0.5-1
- Initial package.
- Pulled in rtm script (command-line frontend to module).
- Patched rtm script to support American English spelling. :)
