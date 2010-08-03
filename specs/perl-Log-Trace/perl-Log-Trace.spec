# $Id$
# Authority: shuff
# Upstream: BBC <cpan$bbc,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Trace

Summary: provides a unified approach to tracing
Name: perl-Log-Trace
Version: 1.070
Release: 1%{?dist}
License: unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Trace/

Source: http://search.cpan.org/CPAN/authors/id/B/BB/BBC/Log-Trace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
A module to provide a unified approach to tracing. A script can use Log::Trace
qw( < mode > ) to set the behaviour of the TRACE function.

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
%doc Changes COPYING META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Log/Trace.pm
%{perl_vendorlib}/Log/Trace/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Aug 03 2010 Steve Huff <shuff@vecna.org> - 1.070-1
- Initial package.
