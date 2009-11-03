# $Id$
# Authority: dag
# Upstream: Jiri Denemark <jirka$ics,muni,cz>

Summary: Tool for transporting data over the internet
Name: netrw
Version: 1.3.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.fi.muni.cz/~xdenemar/netrw/

Source: http://www.fi.muni.cz/~xdenemar/files/netrw/netrw-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
netrw is a simple (but powerful) tool for transporting data over the
internet. Its main purpose is to simplify and speed up file transfers
to hosts without an FTP server. It can also be used for uploading data
to some other user.

It is something like one-way netcat (nc) with some nice features
concerning data transfers. Netrw can compute and check message digest
(MD5, SHA-1, and some others) of all the data being transferred, it
can also print information on progress and average speed.  At the end
it sums up the transfer.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README THANKS
%{_bindir}/netread
%{_bindir}/netwrite
%{_bindir}/nr
%{_bindir}/nw

%changelog
* Wed Aug 16 2006 Dag Wieers <dag@wieers.com> - 1.3.2-1
- Updated to release 1.3.2.

* Sun Mar 05 2006 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Updated to release 1.3.1.

* Tue Feb 07 2006 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
