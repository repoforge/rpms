# $Id$
# Authority: shuff
# Upstream: W3C QA-dev Team <public-qa-dev$w3,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name W3C-LogValidator

Summary: The W3C Log Validator
Name: perl-%{real_name}
Version: 1.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/W3C-LogValidator/

Source: http://search.cpan.org/CPAN/authors/id/O/OL/OLIVIERT/LogValidator/W3C-LogValidator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Config::General)
BuildRequires: perl(DB_File)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Mail::Sendmail)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(URI::Escape)
BuildRequires: rpm-macros-rpmforge
Requires: perl
BuildRequires: perl(Config::General)
BuildRequires: perl(DB_File)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Temp)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Mail::Sendmail)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(URI::Escape)

Provides: %{_bindir}/logprocess.pl

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
W3C::LogValidator is the main module for the W3C Log Validator, a combination
of Web Server log analysis and statistics tool and Web Content quality checker.

The W3C::LogValidator can batch-process a number of documents through a number
of quality focus checks, such as HTML or CSS validation, or checking for broken
links. It can take a number of different inputs, ranging from a simple list of
URIs to log files from various Web servers. And since it orders the result
depending on the number of times a document appears in the file or logs, it is,
in practice, a useful way to spot the most popular documents that need work.

the perl script logprocess.pl, bundled in the W3C::LogValidator distribution,
is a simple way to use the features of W3C::LogValidator. Developers can also
use W3C::LogValidator can be used as a perl module to build applications.

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
%doc Changes MANIFEST README
%doc samples/
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/W3C/
%{perl_vendorlib}/W3C/*
%{_bindir}/*

%changelog
* Tue Mar 09 2010 Steve Huff <shuff@vecna.org> - 1.4-1
- Initial package.
