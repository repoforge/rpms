# $Id$
# Authority: dag
# Upstream: Russell Coker <russell$coker,com,au>

Summary: Benchmark suite for hard drive and file system performance
Name: bonnie++
Version: 1.96
Release: 1
License: GPL
Group: Applications/System
URL: http://www.coker.com.au/bonnie++/

Source: http://www.coker.com.au/bonnie++/experimental/bonnie++-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Bonnie++ is a benchmark suite that is aimed at performing a number of
simple tests of hard drive and file system performance. Then you can
decide which test is important and decide how to compare different
systems after running it. I have no plans to ever have it produce a
single number, because I don't think that a single number can be useful
when comparing such things.

%prep
%setup

%{__perl} -pi.orig -e '
        s|\$\(eprefix\)/sbin|\$(sbindir)|;
        s|\$\(eprefix\)/bin|\$(bindir)|;
        s|\@mandir\@|\$(mandir)|;
    ' Makefile.in

%{__cat} <<EOF >>getc_putc.h
#define min(x1,x2) ((x1) > (x2))? (x2):(x1)
#define max(x1,x2) ((x1) > (x2))? (x1):(x2)
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man8/
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changelog.txt copyright.txt credits.txt readme.html README.txt
%doc %{_mandir}/man1/bon_csv2html.1*
%doc %{_mandir}/man1/bon_csv2txt.1*
%doc %{_mandir}/man1/generate_randfile.1*
%doc %{_mandir}/man8/bonnie++.8*
%doc %{_mandir}/man8/getc_putc.8*
%doc %{_mandir}/man8/zcav.8*
%{_bindir}/bon_csv2html
%{_bindir}/bon_csv2txt
%{_bindir}/generate_randfile
%{_sbindir}/bonnie++
%{_sbindir}/getc_putc
%{_sbindir}/getc_putc_helper
%{_sbindir}/zcav

%changelog
* Fri Jul 10 2009 Dag Wieers <dag@wieers.com> - 1.96-1
- Updated to release 1.96.

* Sun Nov 09 2008 Dag Wieers <dag@wieers.com> - 1.94-1
- Updated to release 1.94.

* Sat Nov 08 2008 Dag Wieers <dag@wieers.com> - 1.03d-1
- Updated to release 1.03d.

* Fri Apr 16 2004 Dag Wieers <dag@wieers.com> - 1.03-1.a
- Initial package. (using DAR)
