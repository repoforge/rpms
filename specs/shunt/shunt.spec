# $Id$
# Authority: dag
# Upstream: Paul Serice <paul$serice,net>

Summary: Shunt data around closed pipes to restarted processes.
Name: shunt
Version: 1.7.2
Release: 1
License: GPL
Group: Applications/System
URL: http://www.serice.net/shunt/

Source: http://www.serice.net/shunt/shunt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
shunt is a general purpose command-line tool that is used to shunt data around
closed pipes to restarted processes. By creative use of the scripts that are
restarted or by recursively calling shunt, you should be able to do some
interesting things, but I wrote it primarily to allow me to stream multi-volume
data backups directly to CD or DVD without the need for any temporary files on
disk.

exactly is a trivial program that is used to exactly control the number of bytes
consumers in the pipeline consume. This is especially useful when dealing with
programs that use the buffered C/C++ standard I/O library or when you want an
unbuffered program to be less greedy. You need to use this program with mkisofs
(but not with the included flyisofs that serves the same purpose).

flyisofs creates an ISO 9660 file system on the fly from a stream of data on
standard input. The data is stored sequentially in files the size of your
choosing.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 bin/exactly %{buildroot}%{_bindir}/exactly
%{__install} -Dp -m0755 bin/flyisofs %{buildroot}%{_bindir}/flyisofs
%{__install} -Dp -m0755 bin/shunt %{buildroot}%{_bindir}/shunt

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL.TXT LICENSE.TXT README.TXT
%{_bindir}/exactly
%{_bindir}/flyisofs
%{_bindir}/shunt

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 1.7.2-1
- Initial package. (using DAR)
