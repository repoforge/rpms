# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME-Encodings

Summary: A unified interface to MIME encoding and decoding
Name: perl-Email-MIME-Encodings
Version: 1.3
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME-Encodings/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/C/CW/CWEST/Email-MIME-Encodings-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module simply wraps "MIME::Base64" and "MIME::QuotedPrint" so that
you can throw the contents of a "Content-Transfer-Encoding" header at
some text and have the right thing happen.

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
%dir %{perl_vendorlib}/Email/MIME/
%{perl_vendorlib}/Email/MIME/Encodings.pm

%changelog
* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
