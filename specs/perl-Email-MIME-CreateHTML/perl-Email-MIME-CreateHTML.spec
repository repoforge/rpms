# $Id$
# Authority: dag
# Upstream: BBC (British Broadcasting Corporation) <cpan$bbc,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME-CreateHTML

Summary: Multipart HTML Email builder
Name: perl-Email-MIME-CreateHTML
Version: 1.030
Release: 1%{?dist}
License: unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME-CreateHTML/

Source: http://search.cpan.org/CPAN/authors/id/B/BB/BBC/Email-MIME-CreateHTML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::Serializer)
BuildRequires: perl(Email::MIME::Creator)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Slurp::WithinPolicy)
BuildRequires: perl(HTML::Tagset)
BuildRequires: perl(HTML::TokeParser::Simple) >= 3.15
BuildRequires: perl(Log::Trace)
BuildRequires: perl(MIME::Types)
#BuildRequires: perl(Test::Assertions)
#BuildRequires: perl(Test::Assertions::TestScript)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Data::Serializer)
Requires: perl(Email::MIME::Creator)
Requires: perl(File::Slurp::WithinPolicy)
Requires: perl(HTML::Tagset)
Requires: perl(HTML::TokeParser::Simple) >= 3.15
Requires: perl(Log::Trace)
Requires: perl(MIME::Types)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module allows you to build HTML emails, optionally with a text-only
alternative and embedded media objects. For example, an HTML email with an
alternative version in plain text and with all the required images contained in
the mail.

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
%doc COPYING Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Email/MIME/CreateHTML/
%{perl_vendorlib}/Email/MIME/CreateHTML.pm

%changelog
* Tue Aug 03 2010 Steve Huff <shuff@vecna.org> - 1.030-1
- Updated to version 1.030.
- Captured dependencies.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 1.026-1
- Initial package. (using DAR)
