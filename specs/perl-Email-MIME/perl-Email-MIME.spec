# $Id$

# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define real_name Email-MIME
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Easy MIME message parsing
Name: perl-Email-MIME
Version: 1.82
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/C/CW/CWEST/Email-MIME-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is an extension of the Email::Simple module, to handle MIME encoded
messages. It takes a message as a string, splits it up into its
constituent parts, and allows you access to various parts of the
message. Headers are decoded from MIME encoding.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Email/MIME.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.82-1
- Initial package.

