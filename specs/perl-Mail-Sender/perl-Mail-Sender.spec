# $Id$

# Authority: dries
# Upstream:

%define real_name Mail-Sender
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

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
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/Mail/Sender/CType/Win32.pm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Mail/Sender.pm
%{perl_vendorlib}/Mail/Sender
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist
%exclude %{perl_vendorlib}/Mail/Sender/CType/Win32.pm

%changelog
* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.8.10-1
- Initial package.
