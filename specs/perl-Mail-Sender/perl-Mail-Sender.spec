# $Id: $

# Authority: dries
# Upstream:

%define real_name Mail-Sender

Summary: Module for sending mails with attachments
Name: perl-Mail-Sender
Version: 0.8.10
Release: 1
License: Other
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Sender/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JENDA/Mail-Sender-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Requires: perl

%description
Mail::Sender is a module for sending mails with attachments through an SMTP
server.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
echo "N" | %{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Mail/Sender/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{_libdir}/perl5/vendor_perl/*/Mail/Sender.pm
%{_libdir}/perl5/vendor_perl/*/Mail/Sender

%changelog
* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.8.10-1
- Initial package.
