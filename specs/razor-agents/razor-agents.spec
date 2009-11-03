# $Id$
# Authority: dag

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Use the Razor catalog server to filter spam messages
Name: razor-agents
Version: 2.84
Release: 1%{?dist}
License: Artistic
Group: Applications/Internet
URL: http://razor.sourceforge.net/

Source: http://dl.sf.net/razor/razor-agents-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(Net::DNS), perl(Digest::SHA1), perl(Time::HiRes), perl(MIME::Base64), perl-URI
Requires: perl-Razor-Agent = %{version}-%{release}

%description
Vipul's Razor is a distributed, collaborative, spam detection and filtering
network.  Razor establishes a distributed and constantly updating catalogue of
spam in propagation.  This catalogue is used by clients to filter out known
spam.  On receiving a spam, a Razor Reporting Agent (run by an end-user or a
troll box) calculates and submits a 20-character unique identification of the
spam (a SHA Digest) to its closest Razor Catalogue Server.  The Catalogue
Server echos this signature to other trusted servers after storing it in its
database.  Prior to manual processing or transport-level reception, Razor
Filtering Agents (end-users and MTAs) check their incoming mail against a
Catalogue Server and filter out or deny transport in case of a signature
match.  Catalogued spam, once identified and reported by a Reporting Agent,
can be blocked out by the rest of the Filtering Agents on the network.

%package -n perl-Razor-Agent
Group: Applications/CPAN
Summary: perl-Razor Perl module
Requires: perl(Net::DNS)
Obsoletes: razor-agents-sdk, perl-Razor

%description -n perl-Razor-Agent
Implements perl class Razor, a SPAM/UCE filtering agent.

%prep
%setup

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS="vendor"
cd Razor2-Preproc-deHTMLxs
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor"
cd -
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
%{__mv} -f Changes Changes.pod
pod2text Changes.pod > Changes

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PERL_INSTALL_ROOT="%{buildroot}" \
	PERL5LIB="%{buildroot}%{perl_vendorarch}" \
	INSTALLMAN5DIR="%{_mandir}/man5"
%makeinstall -C Razor2-Preproc-deHTMLxs PERL_INSTALL_ROOT="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_bindir}
#for bin in razor-check razor-report razor-admin razor-revoke; do
#    %{__ln_s} -f razor-client %{buildroot}%{_bindir}/$bin
#done
%{__rm} -Rf %{buildroot}%{perl_vendorarch}/auto/*/.packlist %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changes CREDITS FAQ INSTALL README docs/
%doc %{_mandir}/man1/razor-*.1*
%doc %{_mandir}/man5/razor-*.5*
%{_bindir}/razor-admin
%{_bindir}/razor-check
%{_bindir}/razor-client
%{_bindir}/razor-report
%{_bindir}/razor-revoke

%files -n perl-Razor-Agent
%defattr(-, root, root, 0755)
%doc BUGS Changes CREDITS FAQ INSTALL README docs/
%doc %{_mandir}/man3/Razor2::*.3pm*
%{perl_vendorlib}/Razor2/
%{perl_vendorlib}/auto/Razor2/
%{perl_vendorarch}/Razor2/
%{perl_vendorarch}/auto/Razor2/

%changelog
* Fri Sep 28 2007 Dag Wieers <dag@wieers.com> - 2.84-1
- Updated to release 2.84.

* Fri Jan 19 2007 Dag Wieers <dag@wieers.com> - 2.82-1
- Updated to release 2.82.

* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 2.81-2
- Fix: the commands aren't links to razor-client anymore, thanks to subs at jake8us org.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.81-1
- Updated to release 2.81.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 1.20-0
- Initial package. (using DAR)
