# $Id$
# Authority: dries
# Upstream: Ryan Eatmon <reatmon$mail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-XMPP

Summary: XMPP Perl Library
Name: perl-Net-XMPP
Version: 1.0
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-XMPP/

Source: http://www.cpan.org/modules/by-module/Net/Net-XMPP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
The Extensible Messaging and Presence Protocol (XMPP) is an IETF standard
that provides a complete cross protocol messaging solution.  The problem
with current IM solutions is that they are all proprietary and cannot
talk to each other.  XMPP seeks to get rid of those barriers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/XMPP.pm
%{perl_vendorlib}/Net/XMPP/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.

