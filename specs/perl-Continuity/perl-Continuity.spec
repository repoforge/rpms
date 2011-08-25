# $Id$
# Authority: shuff
# Upstream: Brock Wilcox <awwaiid$thelackthereof,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Continuity

Summary: Abstract away statelessness of HTTP, for stateful Web applications
Name: perl-%{real_name}
Version: 1.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Continuity/

Source: http://search.cpan.org/CPAN/authors/id/A/AW/AWWAIID/Continuity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Coro) >= 4.37
BuildRequires: perl(Coro::Event)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Daemon) >= 1.36
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Coro) >= 4.37
Requires: perl(Coro::Event)
Requires: perl(HTTP::Daemon) >= 1.36
Requires: rpm-macros-rpmforge

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Continuity is a library to simplify web applications. Each session is written
and runs as a persistant application, and is able to request additional input
at any time without exiting. This is significantly different from the
traditional CGI model of web applications in which a program is restarted for
each new request.

The program is passed a $request variable which holds the request (including
any form data) sent from the browser. In concept, this is a lot like a $cgi
object from CGI.pm with one very very significant difference. At any point in
the code you can call $request->next. Your program will then suspend, waiting
for the next request in the session. Since the program doesn't actually halt,
all state is preserved, including lexicals -- getting input from the browser is
then similar to doing $line = <> in a command-line application.

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
%doc Changes MANIFEST META.yml README doc/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Continuity.pm
%{perl_vendorlib}/Continuity/*

%changelog
* Thu Aug 25 2011 Steve Huff <shuff@vecna.org> - 1.4-1
- Update to version 1.4.

* Mon Jan 04 2010 Steve Huff <shuff@vecna.org> - 1.01-1
- Initial package.
