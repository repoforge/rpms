# $Id$
# Authority: dries
# Upstream: Ryan Eatmon <reatmon$mail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Jabber

Summary: Jabber protocol interface
Name: perl-Net-Jabber
Version: 2.0
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Jabber/

Source: http://www.cpan.org/modules/by-module/Net/Net-Jabber-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Jabber Instant Messaging project is an Open Source project seeking
to provide a complete cross protocol messaging solution.  The problem
with current IM solutions is that they are all proprietary and cannot
talk to each other.  Jabber seeks to get rid of those barriers by
allowing a Jabber client to talk with an AOL user, or an IRC chat room,
or any number of other programs.

For more information about the Jabber project visit http://www.jabber.org.

Net::Jabber is a collection of Perl modules that provide a Perl Developer
access to the Jabber protocol.  Using OOP modules we provide a clean
interface to writing anything from a full client to a simple protocol
tester.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/Net/Jabber.pm
%{perl_vendorlib}/Net/Jabber/*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.0-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Updated to release 2.0.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.30-1
- Initial package.
