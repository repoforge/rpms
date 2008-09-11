# $Id$
# Authority: dag
# Upstream: 

Summary: Friendly greeting program
Name: hello
Version: 2.3
Release: 1
License: GPL
Group: Development/Tools
URL: http://www.gnu.org/software/hello/

Source0: http://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz
Patch0: hello-2.3-earth.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: make
Requires: info

Provides: gnu-hello
Obsoletes: microsoft-hello
Conflicts: bsd-hello

%description
The GNU `hello' program produces a familiar, friendly greeting.  It
allows nonprogrammers to use a classic computer science tool which
would otherwise be unavailable to them.  Because it is protected by the
GNU General Public License, users are free to share and change it.

GNU hello supports many a lot native languages.

%prep
%setup
#patch0 -p0

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%post
#/sbin/ldconfig
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%postun
#/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_infodir}/*.gz
%doc %{_mandir}/man1/hello.1*
%{_bindir}/hello

%changelog
* Wed Aug 20 2008 Dag Wieers <dag@wieers.com> - 2.3-1
- Initial package.
