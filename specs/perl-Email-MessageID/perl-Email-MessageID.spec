# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MessageID

Summary: Generate world unique message-ids
Name: perl-Email-MessageID
Version: 1.35
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MessageID/

Source: http://www.cpan.org/modules/by-module/Email/Email-MessageID-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Message-ids are optional, but highly recommended, headers that identify
a message uniquely. This software generates a unique message-id. This
module generates world unique message-ids.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/MessageID.pm

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.35-1
- Updated to release 1.35.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.31-1.2
- Rebuild for Fedora Core 5.

* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.31-1
- Initial package.
