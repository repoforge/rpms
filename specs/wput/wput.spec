# $Id$
# Authority: dries
# Upstream: Hagen Fritsch <itooktheredpill$gmx,de>

Summary: Uploads files to FTP servers
Name: wput
Version: 0.6.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://wput.sourceforge.net/

Source: http://dl.sf.net/wput/wput-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
Wput is the opposite of wget, capable of uploading files to FTP servers 
with an easy to use command line interface similar to wget's interface.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1
%{__make} install DESTDIR="%{buildroot}" bindir="%{buildroot}%{_bindir}" mandir="%{buildroot}%{_mandir}/man1/"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL TODO
%doc %{_mandir}/man1/wput.1*
%{_bindir}/wput

%changelog
* Sun Dec 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.6.1-1
- Initial package.
