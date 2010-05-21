# $Id$
# Authority: shuff
# Upstream: Vlatko Kosturjak <kost$linux,hr>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Nessus-XMLRPC

Summary: Communicate with Nessus scanner(v4.2+) via XMLRPC
Name: perl-%{real_name}
Version: 0.30
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Nessus-XMLRPC/

Source: http://search.cpan.org/CPAN/authors/id/K/KO/KOST/Net-Nessus-XMLRPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::Simple)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(HTTP::Request::Common)
# we need either Net::SSL or IO::Socket::SSL
# Requires: perl(IO::Socket::SSL)
Requires: perl(LWP::UserAgent)
Requires: perl(Net::SSL)
Requires: perl(XML::Simple)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This is Perl interface for communication with Nessus scanner over XMLRPC. You
can start, stop, pause and resume scan. Watch progress and status of scan,
download report, etc.

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
%doc Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Net/Nessus/
%{perl_vendorlib}/Net/Nessus/*

%changelog
* Fri May 21 2010 Steve Huff <shuff@vecna.org> - 0.30-1
- Updated to version 0.30.

* Tue May 04 2010 Steve Huff <shuff@vecna.org> - 0.20-1
- Initial package.
