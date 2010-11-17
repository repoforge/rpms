# $Id$
# Authority: dries
# Upstream: Ryan Eatmon <reatmon$mail,com>

### EL6 ships with perl-Net-XMPP-1.02-8.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-XMPP

Summary: XMPP Perl Library
Name: perl-Net-XMPP
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-XMPP/

Source: http://www.cpan.org/modules/by-module/Net/Net-XMPP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker), perl(Module::Build)

%description
The Extensible Messaging and Presence Protocol (XMPP) is an IETF standard
that provides a complete cross protocol messaging solution.  The problem
with current IM solutions is that they are all proprietary and cannot
talk to each other.  XMPP seeks to get rid of those barriers.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE.LGPL MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Net::XMPP.3pm*
%doc %{_mandir}/man3/Net::XMPP::*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/XMPP/
%{perl_vendorlib}/Net/XMPP.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
